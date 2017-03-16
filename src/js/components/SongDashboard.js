import React from 'react';
import SongNavigation from './SongNavigation';
import { PageHeader, Grid, Breadcrumb } from 'react-bootstrap';

const SongDashboard = ({ songs }) => (
	<Grid fluid={true}>
		<Breadcrumb>
            <Breadcrumb.Item>
                Home
            </Breadcrumb.Item>
            <Breadcrumb.Item>
                Songs
            </Breadcrumb.Item>           
        </Breadcrumb>
		<PageHeader>Songs{ songs ? ': ' + songs.length : null } </PageHeader>
		<SongNavigation songs={songs} />
	</Grid>
);
export default SongDashboard;

