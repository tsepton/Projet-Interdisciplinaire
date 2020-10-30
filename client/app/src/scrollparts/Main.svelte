<script>
  import Map from "../components/Map.svelte";
  import GeojsonPoints from "../components/GeojsonPoints.svelte";
  import GeojsonLines from "../components/GeojsonLines.svelte";
  import Filter from "../components/Filter.svelte";
  import Card from "../components/Card.svelte";
  import { shapefiles } from "../lib/api";
  import App from "../App.svelte";

  let actuStops = shapefiles("actu_stops");
  let actuLines = shapefiles("actu_lines");
  let geojsons;

  $: geojsons = Promise.allSettled([actuStops, actuLines]);
</script>

<style>
  main {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    max-width: 100%;
    height: fit-content;
    min-height: 100vh;
    column-gap: 2rem;
  }
  /* Small screens */
  @media (max-width: 900px) {
    main {
      margin-left: 5px;
      margin-right: 5;
    }
    .grid-container {
      flex-basis: 100%;
      height: 85vh;
      width: 95%;
      margin: 25px;
    }
  }
  /* Large screens */
  @media (min-width: 900px) {
    main {
      margin-left: 5px;
      margin-right: 5;
    }
    .grid-container {
      flex-basis: 45%;
      height: 85vh;
      width: 45%;
    }
  }
  .shadow {
    box-shadow: 0 0 5px 2px var(--secondary);
  }
</style>

<main>
  <div class="grid-container shadow">
    <Map lat={50.842912} lon={4.377492} zoom={10.9}>
      {#await geojsons}
        <div class="grid-container"><b>loading...</b></div>
      {:then data}
        <GeojsonPoints points={data[0].value} />
        <GeojsonLines lines={data[1].value} />
      {:catch error}
        {console.error(error)}
      {/await}
    </Map>
  </div>
  <div class="grid-container shadow">
    <Card header="Information">
      {#await geojsons}
        <div class="grid-container"><b>loading...</b></div>
      {:then data}
        <Filter points={data[0].value} lines={data[1].value} />
      {:catch error}
        {console.error(error)}
      {/await}
    </Card>
  </div>
</main>
