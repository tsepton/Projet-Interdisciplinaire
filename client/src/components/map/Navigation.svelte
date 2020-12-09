<script>
  import { getContext } from "svelte";
  import { key, mapbox } from "../../lib/mapbox.js";

  const { getMap } = getContext(key);
  const map = getMap();

  let position = "bottom-left";

  const nav = new mapbox.NavigationControl();
  map.addControl(nav, position);
</script>
