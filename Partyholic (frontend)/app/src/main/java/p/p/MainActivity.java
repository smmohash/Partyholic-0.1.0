package p.p;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.FileProvider;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.location.Location;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.google.android.gms.maps.model.LatLng;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MainActivity extends AppCompatActivity {

    private static final int REQUEST_CODE_GALLERY = 0;
    private static final int REQUEST_CODE_CAMERA = 1;
    private static Bitmap bitmap;
    private static String date;
    private static boolean loading;
    private static MapFragment fragment;
    private static String time;
    private static Location destination;
    private static double latitude;
    private static double longitude;
    private static boolean sorryNotFound = false;


    // PERMISSION & INITIALIZING MAP FRAGMENT ------------------------------------------------------
/*  All possible method run sequences:
    - onCreate --> checkPermissionThenInitialize --> onRequestPermissionsResult --> initializePlease
        this means that the permissions were not given yet, the app asked the user for them,
        and the user gave them.
    - onCreate --> checkPermissionThenInitialize --> initializePlease
        this means that the permissions were given already at some time in the past by the user,
        so we go directly to main activity.
    - onCreate --> checkPermissionThenInitialize --> onRequestPermissionsResult
        this means that the permissions were not given, the app asked the user for them,
        but the user declined. Now the user is stuck on the "start" screen and they have only two
        options: either close the app, or click "start" and get asked for permissions again.
 */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.checkPermissionThenInitialize();
    }

    public void checkPermissionThenInitialize() {
        // default is to show permission button. If permissions are given, we show main activity:
        setContentView(R.layout.activity_permissions);
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.
                ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
                ActivityCompat.checkSelfPermission(this, Manifest.permission.
                        ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
                ActivityCompat.checkSelfPermission(this, Manifest.permission.
                        WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(this, Manifest.permission.
                READ_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED
        ) {
            this.initializePlease();
        } else {
            ActivityCompat.requestPermissions(this, new String[]{
                    Manifest.permission.ACCESS_COARSE_LOCATION,
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE,
                    Manifest.permission.READ_EXTERNAL_STORAGE,
                    Manifest.permission.INTERNET,
            }, 1);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != 1
                || grantResults.length <= 0
                || grantResults[0] != PackageManager.PERMISSION_GRANTED
                || grantResults[1] != PackageManager.PERMISSION_GRANTED
                || grantResults[2] != PackageManager.PERMISSION_GRANTED
                || grantResults[3] != PackageManager.PERMISSION_GRANTED
                || grantResults[4] != PackageManager.PERMISSION_GRANTED) {
            Toast.makeText(this, "PERMISSION DENIED !",
                    Toast.LENGTH_SHORT).show();
        } else {
            this.initializePlease();
        }
    }

    public void initializePlease() {
        // we are not interacting with the server yet (this will help later for the loading
        // screen) :
        MainActivity.loading = false;
        //hide the top bar that has the app name
        getSupportActionBar().setDisplayShowHomeEnabled(false);
        getSupportActionBar().hide();
        getSupportActionBar().setTitle("Partyholic");
        //initialize destination:
        MainActivity.destination= new Location("");

        //since permissions are given, now we can finally go to main activity:
        setContentView(R.layout.activity_main);
    }

    public void onClickStart(View view) {
        this.checkPermissionThenInitialize();
    }

    File photoFileForCam = null;
    String currentPhotoPathForCam;

    // CAMERA BUTTON & GALLERY BUTTON
    public void onClickCamera(View view) {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        // Ensure that there's a camera activity to handle the intent
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            try {
                String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
                String imageFileName = "JPEG_" + timeStamp + "_";
                File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
                File image = File.createTempFile(imageFileName, ".jpg", storageDir );

                // Save a file: path for use with ACTION_VIEW intents
                currentPhotoPathForCam = image.getAbsolutePath();
                photoFileForCam =image;
            } catch (IOException ex) {
            }
            // Continue only if the File was successfully created
            if (photoFileForCam != null) {
                Uri photoURI = FileProvider.getUriForFile(this,
                        "com.example.android.fileprovider",
                        photoFileForCam);
                takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI);
                startActivityForResult(takePictureIntent, REQUEST_CODE_CAMERA);
            }
        }
    }

    public void onClickGallery(View view) {
        Intent photoPickerIntent = new Intent(Intent.ACTION_PICK);
        photoPickerIntent.setType("image/*");
        startActivityForResult(photoPickerIntent, REQUEST_CODE_GALLERY);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != RESULT_OK) return;
        if (requestCode == REQUEST_CODE_CAMERA) {
            // Get the dimensions of the bitmap
            BitmapFactory.Options bmOptions = new BitmapFactory.Options();
            bmOptions.inJustDecodeBounds = true;

            BitmapFactory.decodeFile(currentPhotoPathForCam, bmOptions);
            // Decode the image file into a Bitmap sized to fill the View
            bmOptions.inJustDecodeBounds = false;
            bmOptions.inSampleSize = 1;
            bmOptions.inPurgeable = true;

            MainActivity.bitmap = BitmapFactory.decodeFile(currentPhotoPathForCam, bmOptions);
            // try to delete the currentPhotoPath
            File toBeDeleted = new File(currentPhotoPathForCam);
            toBeDeleted.delete();
        } else if (requestCode == REQUEST_CODE_GALLERY) {
            Uri imageUri = data.getData();
            InputStream imageStream = null;
            try {
                imageStream = getContentResolver().openInputStream(imageUri);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            MainActivity.bitmap = BitmapFactory.decodeStream(imageStream);
        }
        /* if you forget to do "setContentView(R.layout.activity_confirm)", not only the screen
        stays on wrong activity, but you also get a nullpointerexception because "findViewById"
        won't even find "imageview" */
        setContentView(R.layout.activity_confirm);
        ImageView imageView = findViewById(R.id.image_view);
        imageView.setImageBitmap(bitmap);
    }

    // YES BUTTON & NO BUTTON & BACK BUTTON --------------------------------------------------------
    public void onClickNo(View view) {
        setContentView(R.layout.activity_main);
    }

    @Override
    public void onBackPressed() {
        if (!MainActivity.loading) setContentView(R.layout.activity_main);
    }

    public void onClickYes(View view) {
        // It takes a long time to send and receive info. So, we prevent the user from escaping
        // the loading screen and sending another request while the current request is still being
        // worked on. So, this disables the back button:
        MainActivity.loading = true;

        //go to loading screen:
        setContentView(R.layout.activity_loading);

        // send the file located in "outFile" to the server:
        new DealingWithServerTask().execute();
    }


    //https://www.youtube.com/watch?v=xXkjfnhqRGI
    @SuppressLint("StaticFieldLeak")
    private class DealingWithServerTask extends AsyncTask<Void, Void, Void> {

        @RequiresApi(api = Build.VERSION_CODES.O)
        @Override
        protected Void doInBackground(Void... voids) {
            try {
                /* ----------- from bitmap to file ----------- */
                // saving image into a directory: creating the directory if not existing:
                FileOutputStream fileOutputStream = null;

                File file = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
                File dir = new File(file.getAbsolutePath() + "/MyPics");
                dir.mkdirs();
                String fileName = String.format("%d.jpg", System.currentTimeMillis());
                File outFile = new File(dir, fileName);

                // saving image into a directory: writing the image from the Bitmap object into a file in
                // the already specified directory:
                /*it is important to reduce the image size
                becase the server will close the connection if it was a huge file !!!!!!!!*/
                //https://stackoverflow.com/questions/38016109/javax-net-ssl-sslexception-write-error-ssl-0x7f70604080-i-o-error-during-syst
                int quality = 60;
                do {
                    fileOutputStream = new FileOutputStream(outFile);
                    MainActivity.bitmap.compress(Bitmap.CompressFormat.JPEG, quality, fileOutputStream);
                    // decease the quality
                    quality -= 10;
                    // finished writing, now close and flush:
                    try {
                        fileOutputStream.flush();
                        fileOutputStream.close();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                } while (outFile.length() > 2000000);


                /* ----------- from file to bytearray ----------- */
                // getting the image path and read it in bytes
                Path path = Paths.get(outFile.getAbsolutePath());
                byte[] fileContents = Files.readAllBytes(path);

                // establishing connection with the API:
                /*HttpURLConnection seems to have replaced the old classic HttpRequest and the
                 * other stuff that comes with it.*/
                URL url = new URL("https://partyholic-eu-v2.herokuapp.com/");
                HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
                httpURLConnection.setRequestMethod("POST");
                httpURLConnection.setRequestProperty("Content-Type", "image/jpeg");
                httpURLConnection.setRequestProperty("Content-Disposition", "form-data;name=imageset");
                httpURLConnection.setDoOutput(true);
                httpURLConnection.setDoInput(true);//#

                // open an outputstream with the connection
                OutputStream out = httpURLConnection.getOutputStream();
                DataOutputStream os = new DataOutputStream(out);

                //https://stackoverflow.com/questions/47355194/java-using-httpurlconnection-to-make-post-request-and-send-image-to-server/52695741
                // writing the image into the data output stream: in other words: sending it!
                os.write(fileContents, 0, fileContents.length);

                // this line should be included ! .    "200" means "ok". So, if not ok, then abort.
                // and set date and time to Unknown so that app doesn't crash by "NullPointerException" on the date
                if (httpURLConnection.getResponseCode() != 200) {
                    System.out.println("SERVER ERROR Connection! : -------------------------------------------------" + httpURLConnection.getResponseCode());
                    MainActivity.date="Unknown";
                    MainActivity.time="Unknown";
                    return null;
                }
                // reading the response (line by line) and saving into a Stringtext.
                BufferedReader bufferedReader;
                bufferedReader = new BufferedReader(new InputStreamReader(httpURLConnection.
                        getInputStream()));
                String responseLine;
                StringBuilder responseWhole = new StringBuilder();
                while ((responseLine = bufferedReader.readLine()) != null) {
                    responseWhole.append(responseLine);
                }
                bufferedReader.close();

                // responseWhole must be parsed with a json parser:
                JSONObject jsonObject = new JSONObject(responseWhole.toString());

                System.out.println("////////////////////////////////////////");
                System.out.println(responseWhole);
                System.out.println("////////////////////////////////////////");

                // finally, getting the values of date, time, and address:
                MainActivity.date = (String) jsonObject.get("date");
                MainActivity.time = (String) jsonObject.get("time");
                if ((int) jsonObject.get("coordinatesAreValid") == 0) {
                    MainActivity.sorryNotFound = true;
                } else {
                    JSONObject coordinateObject = (JSONObject) jsonObject.get("coordinate");
                    System.out.println("----------------------------------------------------");
                    System.out.println(coordinateObject);
                    System.out.println(coordinateObject.get("latitude"));
                    System.out.println(coordinateObject.get("longitude"));
                    System.out.println("----------------------------------------------------");
                    MainActivity.destination.setLatitude((double)coordinateObject.
                            getDouble("latitude"));
                    MainActivity.destination.setLongitude((double)coordinateObject.
                            getDouble("longitude"));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            super.onPostExecute(aVoid);
            // go back from the loading screen, and show the result screen (activity_result),
            // or if no address was found (maybe because the image quality is low), then show
            // "sorry" activity.
            if (MainActivity.sorryNotFound) {
                // important to add ,
                // because if the first tried image was not successfully detected
                // then all the followed images will land on the sorry page
                MainActivity.sorryNotFound=false;
                setContentView(R.layout.activity_sorry);
                return;
            }
            setContentView(R.layout.activity_result);
            //initialize fragment:    (seems that this has to happen every time we switch to
            // activity_result) :
            MainActivity.fragment = new MapFragment(
                    MainActivity.destination, MainActivity.date, MainActivity.time);
            //open fragment:
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.frame_layout, fragment)
                    .commit();
            MainActivity.loading=false;
        }
    }


    public void onClickCurrentLocation(View view) {
        MainActivity.fragment.showCurrentLocation();
    }

    public void onClickDestination(View view) {
        MainActivity.fragment.showDestination();
    }


}