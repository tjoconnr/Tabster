import React from 'react';
import { render } from 'react-dom';
import { Router, Route, Redirect, IndexRedirect, IndexRoute, browserHistory, Link } from 'react-router';

import '../sass/App.sass';
import AppContainer from './containers/AppContainer';
import SongDashboard from './components/SongDashboard';
import SongView from './components/SongView';

render(
  <Router history={browserHistory}>
    <Route path="/a/" component={AppContainer}>
        <IndexRoute component={SongDashboard}  />
        <Route path="/a/song/:songId" component={SongView} />    
        <Redirect from="*" to="/a/" />
    </Route>
  </Router>, document.getElementById('react-app')
);