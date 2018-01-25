
# Our customers are going to buy lots of melons!

melons_to_add = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                 'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                 'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                 'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                 'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                 'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                 'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                 'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                 'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                 'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                 'Watermelon', 'Santa Claus', 'Casaba']


def count_melons(melon_list):
    """Takes in a list, and returns a dictionary with melon counts."""

    melon_counts = {}

    for melon in melon_list:
        if melon in melon_counts:
            melon_counts[melon] = melon_counts[melon] + 1

        else:
            melon_counts[melon] = 1

    return melon_counts

#TRANSLATE THIS PY FUNCT TO JAVASCRIPT

function countMelons(mel_lst) {
    let melon_counts = new Map();

    for (let mel of mel_lst) {
        if (melon_counts.has(mel)) {
            count = melon_counts.get(mel);
            melon_counts.set(mel, count + 1);
        }
        else {
            melon_counts.set(mel, 1);
        }
    }
    return melon_counts
}

#TESTED IN DEV TOOLS IN BROWSER