import React from 'react';
import { render } from 'react-dom';
import { Router, Route, Redirect, IndexRedirect, IndexRoute, browserHistory } from 'react-router';

import { PageHeader } from 'react-bootstrap';

import API from './modules/api';

import '../sass/App.sass';

const AppContainer = React.createClass({
    render() {
        return (
          <div className="container-fluid">
            {this.props.children}
          </div>
        );
    }
});

const DashboardView = React.createClass({

  getInitialState(){
    return {
        user: null,
        auth: null
    }
  },

  renderChildrenWithState() {
    return React.Children.map(this.props.children, (c) => 
      React.cloneElement(c, this.getChildState())
    )
  },

  componentWillMount(){
    this.loadUserData();
    this.loadAuthData();
  },

  render() {
    return (
      <div className="container-fluid">
        {this.renderChildrenWithState()}
      </div>
    );
  },

  loadUserData(){
    API.fetchUser().then(user => {
        this.setState({ user: user });
    }); 
  },

  loadAuthData(){
    API.fetchAuth().then(auth => {
        this.setState({ auth: auth });
    });
  },

  render() {
    const { user, auth} = this.state;
    return (
        <div>
          <PageHeader>Dashboard</PageHeader>
            User: { user ? user.name : '-' }
        </div>
    );
  }
});


render(
  <Router history={browserHistory}>
    <Route path="/a/" component={AppContainer}>
        <IndexRoute component={DashboardView}  />
    </Route>
    <Redirect from="*" to="/a/x" />
  </Router>
, document.getElementById('react-app'));