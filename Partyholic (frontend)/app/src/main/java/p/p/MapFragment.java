package p.p;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import android.os.Looper;
import android.provider.Settings;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationResult;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.concurrent.TimeUnit;

public class MapFragment extends Fragment {

    private final String date;
    private String time;
    private final Location destination;
    private FusedLocationProviderClient fusedLocationProviderClient;
    private SupportMapFragment supportMapFragment;
    public static GoogleMap googleMap;


    MapFragment(Location destination, String date, String time) {
        this.destination = destination;
        this.date = date;
        this.time = time;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        //initialize view:
        View view = inflater.inflate(R.layout.fragment_map, container, false);
        //initialize map fragment:
        this.supportMapFragment = (SupportMapFragment) getChildFragmentManager()
                .findFragmentById(R.id.mapFragment);
        //initialize location client:
        this.fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(getActivity());

        //asynch map:
        supportMapFragment.getMapAsync(new MyOnMapReadyCallback(this,MapFragment.googleMap));

        TextView remaining = view.findViewById(R.id.remaining);
        String toShow;
        // no date has been found
        if (this.date.equals("Unknown")){
            toShow="Whoops , we couldn't find the date of your party!";
            remaining.setText(toShow);
        }else{
            if (this.time.equals("Unknown")) this.time="20:00";
            try {
                String remainingTime= calculateRemainingTime((this.date+" "+this.time));
                toShow= "Time remaining time until your party: \n {0}";

                toShow = java.text.MessageFormat.format(toShow,remainingTime);
                remaining.setText(toShow);
            } catch (ParseException e) {
                e.printStackTrace();
            }
        }

        return view;
    }

    @SuppressLint("MissingPermission") // <-- suppressing this because we already checked for it
    public void showCurrentLocation() {
        //initialize location manager:
        LocationManager locationManager = (LocationManager) getActivity().
                getSystemService(Context.LOCATION_SERVICE);
        //check condition:
        if (locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER) ||
                locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)) {
            fusedLocationProviderClient.getLastLocation().
                    addOnCompleteListener(new OnCompleteListener<Location>() {
                        @Override
                        public void onComplete(@NonNull Task<Location> task) {
                            //initialize location:
                            Location location = task.getResult();

                            // ...
                            if (location != null) {
                                MapFragment.addMarkerAndZoomIn(location);
                            } else {
                                //initialize location request:
                                LocationRequest locationRequest = new LocationRequest()
                                        .setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY)
                                        .setInterval(10000)
                                        .setFastestInterval(1000)
                                        .setNumUpdates(1);
                                //initialize location callback:
                                LocationCallback locationCallback = new LocationCallback() {
                                    @Override
                                    public void onLocationResult(LocationResult locationResult) {
                                        //initialize location:
                                        Location location1 = locationResult.getLastLocation();
                                        MapFragment.addMarkerAndZoomIn(location1);
                                    }
                                };
                                //request location updates:
                                fusedLocationProviderClient.requestLocationUpdates(locationRequest,
                                        locationCallback, Looper.myLooper());
                            }

                        }
                    });
        } else {
            //if location service is not enabled, open location settings:
            startActivity(new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS).
                    setFlags(Intent.FLAG_ACTIVITY_NEW_TASK));
        }
    }

    public void showDestination() {
        MapFragment.addMarkerAndZoomIn(this.destination);
    }


    public static void addMarkerAndZoomIn(Location location){
        System.out.println(location);
        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        MapFragment.addMarkerAndZoomIn(latLng);
    }

    public static void addMarkerAndZoomIn(LatLng latLng){
        //initialize markeroptions:
        MarkerOptions markerOptions = new MarkerOptions();
        //set position of marker:
        markerOptions.position(latLng);
        //set title of marker:
        markerOptions.title(latLng.latitude + " : " + latLng.longitude);
        // remove old markers:
        googleMap.clear();
        //zooming in:
        googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(
                latLng, 18
        ));
        //add marker on map:
        MapFragment.googleMap.addMarker(markerOptions);
    }

// catch it when the date is after the current date time
    private String calculateRemainingTime(String scheduled_date) throws ParseException {
        // date format
        SimpleDateFormat format = new SimpleDateFormat("dd.MM.yyyy HH:mm");
        // two dates
        java.util.Date scheduledDate;
        Calendar current = Calendar.getInstance();
        java.util.Date currentDate;
        String current_date = format.format(current.getTime());
        scheduledDate = format.parse(scheduled_date);
        currentDate = format.parse(current_date);
        long diffInMillie = scheduledDate.getTime() - currentDate.getTime();
        long diffInMinute = TimeUnit.MINUTES.convert(diffInMillie, TimeUnit.MILLISECONDS);
        // if the result is negative then the date is gone
        if (diffInMinute <= 0) return "Sorry but you missed this party";
        // calculate the remaining days , Hours , minutes
        long diffInDays = diffInMinute / (60 * 24) ;
        long restDiffInMinutes = diffInMinute % (60 * 24);
        long restDiffInHours = restDiffInMinutes / 60;
        restDiffInMinutes = restDiffInMinutes % 60;

        System.out.println(diffInMinute);

        return (diffInDays) + " days ,"+(restDiffInHours)+ " hours ,\n" + restDiffInMinutes +" minutes" ;
    }
}