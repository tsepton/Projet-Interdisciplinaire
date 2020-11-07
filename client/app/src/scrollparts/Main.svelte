<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filter from "../components/filters/Filters.svelte";
  import geojsons from "../data/data.js";
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
  <Context>
    <div class="grid-container shadow">
      <Map latitude={50.842912} longitude={4.377492} zoom={10.3}>
        <Stops points={geojsons.stops} />
        <Lines lines={geojsons.lines} />
      </Map>
    </div>
    <div class="grid-container shadow">
      <Filter points={geojsons.stops} lines={geojsons.lines} />
    </div>
  </Context>
</main>
