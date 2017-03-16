import React from 'react';
import SongLink from './SongLink';
import { Nav, NavItem } from 'react-bootstrap';

const SongNavigation = ({ songs }) => (
	<Nav>
		{songs.map((song) => <SongLink key={song._id} song={song} />)}	
	</Nav>
);
export default SongNavigation;