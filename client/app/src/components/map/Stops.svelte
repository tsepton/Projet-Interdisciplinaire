<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  const { getMap, getStops } = getContext(key);
  const map = getMap();
  const stops = getStops();

  map.on("load", () =>
    map.loadImage("/marker.32px.png", (error, image) => {
      if (error) throw error;
      // TODO Visu : Marker
      map.addImage("bus-stop-marker", image);
      map.addSource(`stops-id`, {
        type: "geojson",
        data: stops,
      });
      map.addLayer({
        id: `stops-layer`,
        type: "symbol",
        source: `stops-id`,
        layout: {
          "icon-image": "bus-stop-marker",
          // get the title name from the source's "title" property
          "text-field": ["get", "alpha_fr"],
          "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
          "text-offset": [0, 1.25],
          "text-anchor": "top",
        },
      });
    })
  );
</script>
