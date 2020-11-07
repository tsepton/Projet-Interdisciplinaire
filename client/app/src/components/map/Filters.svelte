<script>
  export let filter = "";
</script>

<style>
  .filter-ctrl {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 10000;
  }

  .filter-ctrl input[type="text"] {
    width: 100%;
    background-color: #fff;
    margin: 0;
    color: rgba(0, 0, 0, 0.5);
    padding: 10px;
    box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1);
    border-radius: 3px;
    width: 180px;
  }
</style>

<div class="filter-ctrl">
  <input
    id="filter-input"
    type="text"
    name="filter"
    placeholder="Filter by name"
    bind:value={filter} />
</div>
