<script>
  import Map from "../components/Map.svelte";
  import MapMarker from "../components/MapMarker.svelte";
</script>

<style>
  main {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    max-width: 100%;
    height: 100vh;
    margin-left: 40px;
    margin-right: 40px;
    column-gap: 2rem;
  }

  /* Small screens */
  @media (max-width: 900px) {
    .grid-container {
      flex-basis: 100%;
      height: 85%;
      width: 95%;
      margin: 25px;
    }
  }
  /* Large screens */
  @media (min-width: 900px) {
    .grid-container {
      flex-basis: 45%;
      height: 85%;
      width: 45%;
    }
  }

  .shadow {
    box-shadow: 0 0 5px 2px var(--secondary);
  }

  .test {
    background-color: var(--primary);
  }
</style>

<main>
  <div class="grid-container shadow">
    <Map lat={50.842912} lon={4.377492} zoom={10.9}>
      <MapMarker lat={50.465856} lon={4.857599} label="UNamur" />
    </Map>
  </div>
  <div class="grid-container test">
    <span>TODO</span>
  </div>
</main>
