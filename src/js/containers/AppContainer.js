import React from 'react';
import AppComponent from '../components/AppComponent';
import API from '../modules/API';

const INITIAL_STATE = {
    user: null,
    songs: [],
    books: []
};

const AppContainer = React.createClass({

  getInitialState(){
    return INITIAL_STATE;
  },

  componentWillMount(){
    this.loadUserData();
    this.loadSongs();    
  },

  loadUserData(){
    API.fetchUser().then(user => {
        this.setState({ user: user });
    }); 
  },

  loadSongs(){
    API.fetchSongs().then(songs => {
        this.setState({ songs: songs });
    });
  },

  getChildState(){
    return { 
      ...this.state
    }
  },

  renderChildrenWithState() {
    return React.Children.map(this.props.children, (c) => 
      React.cloneElement(c, this.getChildState())
    )
  },

  render() {
    const { user, auth, songs } = this.state;
    return (
        <AppComponent props={this.getChildState()} children={this.renderChildrenWithState()} />
    );
  }
});

export default AppContainer;