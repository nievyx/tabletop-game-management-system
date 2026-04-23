import {useEffect, useState} from 'react';
import { get } from '../api/client';
import Profiles from '../components/Profiles';

function ProfilesPage() {
    const [profiles, setProfiles] = useState([]);
    const [loadingProfiles, setLoadingProfiles] = useState(true);

    useEffect(() => {
        get('/profiles')
            .then((data) => {
                setProfiles(data);
                setLoadingProfiles(false);
            })
            .catch((err) => {
                    console.error(err);
                    setLoadingProfiles(false);
            });
        }, []);

    return (
        <Profiles
            profiles={profiles}
            loadingProfiles={loadingProfiles}
        />
    );
}
export default ProfilesPage;