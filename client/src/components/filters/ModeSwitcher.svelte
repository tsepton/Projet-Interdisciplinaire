<script>
  export let mode;

  function handleSelection(selection) {
    mode = selection;
  }
</script>

<style>
  .container {
    width: 100%;
    text-align: center;
    border-radius: 16px;
    box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-around;
    padding-top: 2.8px;
    padding-bottom: 2.8px;
  }

  label {
    margin: auto;
    cursor: pointer;
    color: rgba(0, 0, 0, 0.5);
    text-align: center;
    border-radius: 16px;
    padding-left: 10px;
    padding-right: 10px;
  }

  input {
    display: none;
  }

  input[type="radio"]:checked + label {
    background-color: #ccc;
    font-weight: bold;
  }
</style>

<div class="container">
  <input
    id="mode bus"
    type="radio"
    name="profile"
    checked={mode === 'B' ? true : false}
    on:click={() => handleSelection('B')} />
  <label for="mode bus">Bus</label>
  <input
    id="mode metro"
    type="radio"
    name="profile"
    checked={mode === 'M' ? true : false}
    on:click={() => handleSelection('M')} />
  <label for="mode metro">Métro</label>
  <input
    id="mode tram"
    type="radio"
    name="profile"
    checked={mode === 'T' ? true : false}
    on:click={() => handleSelection('T')} />
  <label for="mode tram">Tram</label>
</div>
