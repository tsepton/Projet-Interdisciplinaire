<script>
  import Filter from "./Filter.svelte";
  import { getContext } from "svelte";
  import { key } from "../../../lib/mapbox.js";

  const { getLines, getStops } = getContext(key);
  const stops = getStops();
  const lines = getLines();
</script>

<style>
  .content {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    background-color: var(--foreground);
  }
  h2 {
    font-size: 2rem;
    font-weight: 200;
  }
  h3 {
    font-size: 1.5rem;
    font-weight: 100;
  }
</style>

<div class="content">
  <h2>Filtrer les informations</h2>
  <hr />
  <Filter features={stops.features} key="alpha_fr">
    <h3 slot="title">Arrêts</h3>
  </Filter>
  <Filter features={lines.features} key="LIGNE">
    <h3 slot="title">Trajets</h3>
  </Filter>
</div>
