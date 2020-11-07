<script>
  import { setContext } from "svelte";
  import { mapbox, key } from "../../lib/mapbox.js";
  import geojsons from "../../data/data.js";

  let map;
  let layers = [];

  const initMap = (latitude, longitude, zoom, container) => {
    map = new mapbox.Map({
      container,
      style: "mapbox://styles/mapbox/light-v10",
      center: [longitude, latitude],
      zoom,
    });
  };

  setContext(key, {
    initMap: initMap,
    getMap: () => map,
    getLines: () => geojsons.lines,
    getStops: () => geojsons.stops,
    getLayers: () => layers,
  });
</script>

<slot />
