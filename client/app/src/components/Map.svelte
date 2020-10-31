<script>
  import { getContext, onMount, setContext } from "svelte";
  import { key } from "../lib/mapbox.js";

  const { getMap, initMap } = getContext(key);

  export let latitude;
  export let longitude;
  export let zoom;

  let container;
  let map;

  onMount(() => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = "https://unpkg.com/mapbox-gl/dist/mapbox-gl.css";
    link.onload = () =>{
      initMap(latitude, longitude, zoom, container);
      map = getMap()
    };
    document.head.appendChild(link);
    return () => {
      map.remove();
      link.parentNode.removeChild(link);
    };
  });
</script>

<style>
  div {
    width: 100%;
    height: 100%;
  }
</style>

<div bind:this={container}>
  {#if map}
    <slot />
  {/if}
</div>
