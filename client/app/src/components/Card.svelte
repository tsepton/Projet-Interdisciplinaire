<style>
  .card {
    border-radius: 1px;
    background-color: var(--foreground);
    width: 100%;
    height: 100%;
    display: inline-block;
  }
  hr {
    height: 10px;
    border: 0;
    box-shadow: 0 10px 10px -10px #8c8b8b inset;
  }
  h1 {
    font-weight: 200;
  }
  .header {
    text-align: center;
  }
</style>

<div class="card">
  <slot name="header" />
  <slot name="body" />
</div>
