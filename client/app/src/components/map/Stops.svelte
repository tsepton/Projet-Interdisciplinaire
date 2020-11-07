<script>
  import { getContext } from "svelte";
  import { key } from "../../lib/mapbox.js";

  const { getMap } = getContext(key);
  const map = getMap();

  export let points;

  map.on("load", () =>
    map.loadImage("/marker.32px.png", (error, image) => {
      if (error) throw error;
      // TODO Visu : Marker
      map.addImage("bus-stop-marker", image);
      map.addSource(`points-id`, {
        type: "geojson",
        data: points,
      });
      map.addLayer({
        id: `points-layer`,
        type: "symbol",
        source: `points-id`,
        layout: {
          "icon-image": "bus-stop-marker",
          // get the title name from the source's "title" property
          "text-field": ["get", "title"],
          "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
          "text-offset": [0, 1.25],
          "text-anchor": "top",
        },
      });
    })
  );
</script>
