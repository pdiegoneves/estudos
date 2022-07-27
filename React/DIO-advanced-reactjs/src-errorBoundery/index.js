import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import ErrorBoundary from './ErrosBoundary'

const main = (
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
)

//nesta data 12/06/2020 não está funcionando, problema na versão do render do react
ReactDOM.render(main, document.getElementById('root'));
// ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
