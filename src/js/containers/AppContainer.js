import React from 'react';
import AppComponent from '../components/AppComponent';
import API from '../modules/API';

const INITIAL_STATE = {
    user: null,
    auth: null,
    songs: [],
    books: []
};

const AppContainer = React.createClass({

  getInitialState(){
    return INITIAL_STATE;
  },

  componentWillMount(){
    this.loadUserData();
    this.loadAuthData();
    this.loadSongs();    
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