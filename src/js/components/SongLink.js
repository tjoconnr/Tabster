import React from 'react';
import { Link } from 'react-router';

const SongLink = ({ song }) => (
	<div>
		{ song ? <Link to={'/a/song/' + song._id}>{song.name}</Link> : null }
	</div>
);
export default SongLink;