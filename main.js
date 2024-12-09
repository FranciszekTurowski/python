
// Funkcja do formatowania daty i godziny
function formatDate(date) {
    return date.toISOString().replace('T', ' ').substring(0, 19);
}

// Pobranie aktualnej daty i godziny
const now = new Date();

// Konwersja na różne strefy czasowe
const utcDate = new Date(now.toUTCString());
const gmtDate = new Date(now.toGMTString());
const cetDate = new Date(now.toLocaleString('en-US', { timeZone: 'CET' }));

// Wyświetlenie wyników w konsoli
console.log("Aktualna data i godzina:");
console.log("UTC: ", formatDate(utcDate));
console.log("GMT: ", formatDate(gmtDate));
console.log("CET: ", formatDate(cetDate));

