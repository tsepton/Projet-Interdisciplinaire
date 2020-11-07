<script>
  import { onMount, getContext, createEventDispatcher } from "svelte";
  import { mapbox, key } from "../../lib/mapbox.js";

  export let filter;

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();
  const dispatch = createEventDispatcher();

  let layerIDs = [];

  $: filter.length, filterStops(filter);

  function filterStops(filter) {
    layerIDs.forEach((layerID) => {
      map.setLayoutProperty(
        layerID,
        "visibility",
        layerID.indexOf(filter.toLowerCase()) > -1 ? "visible" : "none"
      );
    });
  }

  onMount(async () => {
    map.on("load", () => {
      map.loadImage("/marker.32px.png", (error, image) => {
        if (error) throw error;
        // TODO Visu : Marker
        map.addImage("metro-marker", image);

        map.addSource("source-stops", {
          type: "geojson",
          data: stops,
        });

        stops.features.forEach((stop) => {
          const stopID = stop.properties["stop_id"];
          const stopName = stop.properties["alpha_fr"].toLowerCase();
          const layerID = stopName;

          if (!layerIDs.includes(layerID)) {
            map.addLayer({
              id: layerID,
              type: "symbol",
              source: "source-stops",
              layout: {
                "icon-image": "metro-marker",
                // get the title name from the source's "title" property
                "text-field": ["get", "alpha_fr"],
                "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                "text-offset": [0, 1.25],
                "text-anchor": "top",
              },
              filter: ["==", "stop_id", stopID],
            });
            layerIDs = [...layerIDs, layerID];

            // Change the cursor to a pointer when the mouse is over the places layer.
            map.on("mouseenter", layerID, (e) => {
              map.getCanvas().style.cursor = "pointer";
              // Filter lines and remove other stop markers
              dispatch("select", {
                ligne: e.features[0].properties["numero_lig"],
              });
              filter = e.features[0].properties["alpha_fr"].toLowerCase();
            });

            // Change it back to a pointer when it leaves.
            map.on("mouseleave", layerID, (e) => {
              map.getCanvas().style.cursor = "";
              // Remove the  lines filter and re add other stop markers
              dispatch("select", { ligne: "null" });
              filter = "";
            });

            // When a click event occurs on a feature in the places layer, open a popup at the
            // location of the feature, with description HTML from its properties.
            // map.on("click", layerID, (e) => {
              // FIXME : Find proper information to visualise
              // var coordinates = e.features[0].geometry.coordinates.slice();
              // const description = e.features[0].properties.descr_fr;
              // Ensure that if the map is zoomed out such that multiple
              // copies of the feature are visible, the popup appears
              // over the copy being pointed to.
              // while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
              //   coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
              // }
              // new mapbox.Popup()
              //   .setLngLat(coordinates)
              //   .setHTML(description)
              //   .addTo(map);
            // });
          }
        });
      });
    });
  });
</script>
