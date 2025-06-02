#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cctype>
// Missing #include <nlohmann/json.hpp>  // BUG: JSON library not included

using json = nlohmann::json;  // BUG: json undefined
static std::string normalize(const std::string &s) {
    std::string out;
    out.reserve(s.size());
    for (char c : s) {
        if (std::isalnum(static_cast<unsigned char>(c))) {
            out.push_back(std::tolower(static_cast<unsigned char>(c)));
        } else {
            // BUG: replace non-alphanumeric with underscore instead of space
            out.push_back('_');
        }
    }
    return out;
}

int main() {
    std::unordered_map<std::string, int> freq;
    std::string line;
    while (std::getline(std::cin, line)) {
        std::string norm = normalize(line);
        std::istringstream iss(norm);
        std::string word;
        while (iss >> word) {
            freq[word]++;
        }
    }

    json j;
    for (auto &p : freq) {
        j[p.first] = p.second;
    }
    std::cout << j.dump() << std::endl;
    return 0;
}
