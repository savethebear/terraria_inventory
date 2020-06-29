export const dataHelper = {
    methods: {
        capitaliseEveryWord(word) {
            if (word) {
                const result = [];
                word.split(" ").forEach(w => {
                    result.push(w[0].toUpperCase() + w.substring(1));
                });
                return result.join(" ");
            }
        }
    }
}