<script>
  import { setContext } from "svelte";
  import { mapbox, key } from "../lib/mapbox.js";

  let map;

  const initMap = (latitude, longitude, zoom, container) => {
    map = new mapbox.Map({
      container,
      style: "mapbox://styles/mapbox/streets-v9",
      center: [longitude, latitude],
      zoom,
    });
  };

  setContext(key, {
    initMap: initMap,
    getMap: () => map,
  });
</script>

<slot />
