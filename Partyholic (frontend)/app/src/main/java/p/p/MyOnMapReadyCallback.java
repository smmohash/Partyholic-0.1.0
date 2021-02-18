package p.p;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;

public class MyOnMapReadyCallback implements OnMapReadyCallback {
    private MapFragment mapFragment;

    MyOnMapReadyCallback(MapFragment mapFragment, GoogleMap googleMap){
        this.mapFragment=mapFragment;
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        MapFragment.googleMap=googleMap;
        this.mapFragment.showDestination();
    }
}
