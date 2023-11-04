import type { Component } from 'solid-js';
import { Button } from "@suid/material";
import { createResource, Show } from "solid-js";

import logo from './logo.svg';
import styles from './App.module.css';

async function fetchWelcome() {
  const response = await fetch(
    'http://api.fleet.airwarrior.net:3001'
  );
  return await response.json();
}

const [welcome] = createResource(fetchWelcome);

const App: Component = () => {
  return (
    <div class={styles.App}>
      <header class={styles.header}>
        <img src={logo} class={styles.logo} alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          class={styles.link}
          href="https://github.com/solidjs/solid"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn Solid
        </a>
        <Button variant="contained">Hellow World</Button>
        <Show when={!welcome.loading} fallback={<span>loading...</span>}>
          <span>{welcome().detail}</span>
        </Show>
      </header>
    </div>
  );
};

export default App;
