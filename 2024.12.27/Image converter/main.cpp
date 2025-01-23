#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

// Function to read 4 bytes as a little-endian integer
uint32_t readLittleEndian(std::ifstream &file) {
	uint8_t bytes[4];
	file.read(reinterpret_cast<char *>(bytes), 4);
	return bytes[0] | (bytes[1] << 8) | (bytes[2] << 16) | (bytes[3] << 24);
}

int main() {
	std::string filepath = "image.webp";

	// Open the WebP file in binary mode
	std::ifstream file(filepath, std::ios::binary);
	if (!file.is_open()) {
		std::cerr << "Failed to open file: " << filepath << std::endl;
		return 1;
	}

	// Read and validate RIFF header
	char riffHeader[4];
	file.read(riffHeader, 4);
	if (std::string(riffHeader, 4) != "RIFF") {
		std::cerr << "This is not a RIFF file!" << std::endl;
		return 1;
	}

	uint32_t fileSize = readLittleEndian(file);

	char format[4];
	file.read(format, 4);
	if (std::string(format, 4) != "WEBP") {
		std::cerr << "This is not a WEBP file!" << std::endl;
		return 1;
	}

	// Iterate through chunks
	while (file.tellg() < static_cast<std::streampos>(fileSize + 8)) {
		char chunkType[4];
		file.read(chunkType, 4);

		uint32_t chunkSize = readLittleEndian(file);

		// Check if this is the VP8 chunk
		if (std::string(chunkType, 4) == "VP8 ") {
			std::cout << "Found VP8 chunk of size " << chunkSize << std::endl;

			// Read the VP8 chunk data
			std::vector<uint8_t> vp8Data(chunkSize);
			file.read(reinterpret_cast<char *>(vp8Data.data()), chunkSize);

			std::cout << "Read VP8 data successfully!" << std::endl;

			// Process VP8 data here (future steps)
			break;
		} else {
			// Skip non-VP8 chunks
			file.seekg(chunkSize, std::ios::cur);
			if (chunkSize % 2 != 0) {
				file.seekg(1, std::ios::cur); // Skip padding byte
			}
		}
	}

	file.close();
	return 0;
}
