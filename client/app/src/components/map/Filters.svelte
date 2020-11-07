<script>
  export let filter = "";
</script>

<style>
  .filter-ctrl {
    position: absolute;
    z-index: 100 !important;
  }
  .filter-ctrl input[type="text"] {
    width: 100%;
    background-color: #fff;
    margin: 0;
    color: rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 5px 2px var(--secondary);
    border-radius: 3px;
  }
  /* Small screens */
  @media (max-width: 900px) {
    .filter-ctrl {
      width: auto;
      padding: 10px;
      top: 2px;
      right: 2px;
      left: 2px;
    }
  }
  /* Large screens */
  @media (min-width: 900px) {
    .filter-ctrl {
      width: 25%;
      top: 10px;
      right: 10px;
    }
  }
</style>

<div class="filter-ctrl">
  <input
    id="filter-input"
    type="text"
    name="filter"
    placeholder="Chercher une station..."
    bind:value={filter} />
</div>
