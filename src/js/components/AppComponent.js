import React from 'react';

import '../../sass/App.sass';

import NavigationMain from './NavigationMain';

const AppComponent = ({ props, children }) => (
  <div id="app-component">
  	<NavigationMain />
    {children}        
  </div>
);
export default AppComponent;