<script>
  import { getContext } from "svelte";
  import { key, mapbox } from "../../lib/mapbox.js";

  const { getMap } = getContext(key);
  const map = getMap();

  let position = "bottom-right";

  const options = Object.assign({
    maxWidth: 80,
    unit: "metric",
  });

  const scale = new mapbox.ScaleControl(options);
  map.addControl(scale, position);
</script>
