<script>
  export let version;
</script>

<style>
  .Header {
    position: relative;
    height: 100vh;
    display: block;
  }
  .Header-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(19deg, var(--secondary), var(--ternary));
    -webkit-transform-origin: 0px 0px;
    transform-origin: 0px 0px;
    -webkit-transform: skewY(-10deg);
    transform: skewY(-10deg);
    overflow: hidden;
    z-index: -1;
  }
  .Header-content {
    text-align: center;
    padding: 4rem 4rem;
    margin: 0 auto;
  }
  @media (min-width: 58rem) {
    .Header-content {
      text-align: left;
      padding: 10rem 4rem;
      max-width: 54rem;
      display: -webkit-box;
      display: flex;
      -webkit-box-pack: justify;
      justify-content: space-between;
    }
  }
  h1,
  h2,
  p {
    color: #fff;
    text-shadow: 0 0.5rem 1rem rgba(50, 0, 100, 0.1);
  }
  h1 {
    margin: 0;
    font-size: 2.5rem;
    font-weight: 200;
  }
  h2 {
    font-weight: 100;
  }
  p {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    font-weight: 100;
  }
  .Button {
    padding: 1.5rem 2rem;
    border: 0;
    color: var(--quadrary);
    font-size: 1.2rem;
    font-weight: bold;
    background: #fff;
    border-radius: 3px;
    -webkit-transition: all 0.2s;
    transition: all 0.2s;
    cursor: pointer;
    box-shadow: 0 1.75rem 2rem -0.4rem rgba(50, 0, 100, 0.15);
  }
  .Button:hover {
    color: var(--primary);
    box-shadow: 0 1.75rem 3rem 0rem rgba(50, 0, 100, 0.1);
    -webkit-transform: scale(1.05);
    transform: scale(1.05);
  }
  .Button:active {
    box-shadow: 0 1.75rem 2.5rem -0.2rem rgba(50, 0, 100, 0.125);
    -webkit-transform: scale(1.025);
    transform: scale(1.025);
  }
</style>

<!-- Adapted from : https://codepen.io/arthurcamara1/pen/ZXWvOo -->
<div class="Header">
  <div class="Header-background" />
  <div class="Header-content">
    <div>
      <h1>Projet Interdisciplinaire</h1>
      <h2>v{version}</h2>
      <p>Visualisation des trajets de la STIB</p>
      <button
        class="Button"
        on:click={() => window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth',
          })}>Commencer</button>
    </div>
  </div>
</div>
