#	Comando de compilação para o projeto 2 de ASA

# Nome do executável
TARGET = projeto

# Compilador
CXX = g++

# Flags do compilador
CXXFLAGS = -std=c++11 -O3 -Wall -lm

# Ficheiros fonte (adicionar mais ficheiros se necessário)
SRCS = projeto.cpp

# Ficheiros objeto gerados
OBJS = $(SRCS:.cpp=.o)

# Regra principal: compila tudo
all: $(TARGET)

# Regra para criar o executável
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Regra para criar ficheiros objeto a partir de .cpp
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Limpeza dos ficheiros gerados
clean:
	rm -f $(OBJS) $(TARGET)