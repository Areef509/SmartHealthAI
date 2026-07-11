export async function translateText(text, language) {

    if (!text) {
        return "";
    }

    if (language === "en") {
        return text;
    }

    try {

        const response = await fetch(
            `https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=${language}&dt=t&q=${encodeURIComponent(text)}`
        );

        const data = await response.json();

        return data[0][0][0];

    } catch (error) {

        console.error("Translation error:", error);

        return text;
    }
}