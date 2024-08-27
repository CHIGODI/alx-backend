#!usr/bin/node
import { createClient } from 'redis';

const client = await createClient()
    .on('error', err => console.log('Redis client not connected to the server:', err))
    .connect();
console.log('Redis client connected to the server');

const setNewSchool = async (schoolName, value) => {
    const reply = await client.set(schoolName, value);
    console.log(`Reply: ${reply}` );
};

const displaySchoolValue = async (schoolName) => {
    const value = await client.get(schoolName);
    console.log(value);
};

(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
    await client.quit();
})();