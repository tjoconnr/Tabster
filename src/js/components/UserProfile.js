import React from 'react';
import { PageHeader, Grid, Breadcrumb, Row, Col, Jumbotron } from 'react-bootstrap';
import { Link } from 'react-router';

import SongNavigation from './SongNavigation';

const UserProfile = ({ user }) => (
	<Grid fluid={false}>
		<PageHeader>
			Manage Profile
			<div className="pull-right">                
                <h5 style={{marginTop:-5}}>
                    <img src={user ? user.avatar : null } className="img-circle" style={{width:40}} />
                    &nbsp;&nbsp;
                    <strong>{ user ? user.name : ''}</strong>
                </h5>
            </div>
        </PageHeader>
        
	</Grid>
);
export default UserProfile;

