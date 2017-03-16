import React from 'react';
import { render } from 'react-dom';
import { Router, Route, Redirect, IndexRedirect, IndexRoute, browserHistory, Link } from 'react-router';

import AppContainer from './containers/AppContainer';
import SongDashboard from './components/SongDashboard';
import SongView from './components/SongView';
import Home from './components/Home';

window.on
render(
  <Router history={browserHistory}>
    <Route path="/a/" component={AppContainer}>
        <IndexRoute component={Home}  />
        <Route path="/a/songs/" component={SongDashboard} />    
        <Route path="/a/songs/:songId" component={SongView} />    
        <Redirect from="*" to="/a/" />
    </Route>
  </Router>, document.getElementById('react-app')
);