<script>
  import Map from "../components/map/Map.svelte";
  import Context from "../components/map/Context.svelte";
  import Stops from "../components/map/Stops.svelte";
  import Lines from "../components/map/Lines.svelte";
  import Filters from "../components/map/Filters.svelte";

  let filter = "";
</script>

<style>
  main {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    height: fit-content;
    min-height: 100vh;
    /* column-gap: 2rem; */
    margin-left: 2vw;
    margin-right: 2vw;
  }

  .grid-container {
    position: relative;
  }
  /* Small screens */
  /* I left the old flex css in case we need add something else than the map */
  @media (max-width: 900px) {
    main {
      max-width: 100%;
    }
    .grid-container {
      flex-basis: 100%;
      height: 85vh;
      width: 95%;
      /* margin: 25px; */
    }
  }
  /* Large screens */
  @media (min-width: 900px) {
    main {
      max-width: 100%;
    }
    .grid-container {
      flex-basis: 100%;
      height: 85vh;
      width: 95%;
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
        <!-- <Lines /> -->
        <Stops {filter} />
      </Map>
      <Filters bind:filter />
    </div>
  </Context>
</main>
