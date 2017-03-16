import React from 'react';
import SongLink from './SongLink';
import { PageHeader } from 'react-bootstrap';

const SongDashboard = ({ songs }) => (
	<div>
		<PageHeader>Songs{ songs ? ': ' + songs.length : null } </PageHeader>
		{songs.map((song) => <SongLink key={song._id} song={song} /> )}
	</div>
);
export default SongDashboard;

