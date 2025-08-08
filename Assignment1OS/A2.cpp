#include <bits/stdc++.h>
using namespace std;

int main() {
    string paragraph;
    cout << "Enter a paragraph:\n";
    getline(cin, paragraph);

    transform(paragraph.begin(), paragraph.end(), paragraph.begin(), ::tolower);

    for (char &c : paragraph) {
        if (!isalnum(c) && !isspace(c)) {
            c = ' ';
        }
    }

    stringstream ss(paragraph);
    string word;
    map<string, int> freq;

    while (ss >> word) {
        freq[word]++;
    }

    cout << "\nWord Frequencies:\n";
    for (auto &pair : freq) {
        cout << pair.first << ": " << pair.second << "\n";
    }

    return 0;
}
