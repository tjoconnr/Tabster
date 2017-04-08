const API = {
    doFetch(url){
        const fetchSettings = {
            method: 'GET',
            headers: new Headers({
                'Authorization': sessionStorage.getItem('userToken')
            }),
            mode: 'cors',
            cache: 'default' 
        };
        return fetch(url, fetchSettings).then(resp => {
            if (resp.ok) {
                return resp.json();
            }
        }).then(obj => {
            console.log('GET', url, obj);
            return obj;
        });
    },
    fetchUser(){
        return this.doFetch('/api/v1/me');
    },
    fetchSongs(){
        return this.doFetch('/api/v1/song-item');
    },
    fetchSong(songId){
        return this.doFetch('/api/v1/song-item/'+songId);
    }
};
export default API;