$(VERBOSE).SILENT:

<<<<<<< HEAD
# Default target
=======
# default target
>>>>>>> ae84a80... Restructure to be proper package
default: all-install all

ifndef GOPATH
GOPATH := $(shell go env GOPATH)
endif

PROTO_ROOT := .
<<<<<<< HEAD
PROTO_DIRS = $(sort $(dir $(shell find $(PROTO_ROOT) -name "*.proto")))
PROTO_OUT := .gen
PROTO_IMPORT := $(PROTO_ROOT):$(GOPATH)/src/github.com/temporalio/gogo-protobuf/protobuf
=======
# List only subdirectories with *.proto files. Sort to remove duplicates.
PROTO_DIRS = $(sort $(dir $(wildcard $(PROTO_ROOT)/*/*.proto)))
PROTO_SERVICES = $(wildcard $(PROTO_ROOT)/*/service.proto)
PROTO_OUT := .gen
PROTO_IMPORT := $(PROTO_ROOT):$(GOPATH)/src/github.com/gogo/protobuf/protobuf
>>>>>>> ae84a80... Restructure to be proper package

all: grpc

all-install: grpc-install

$(PROTO_OUT):
	mkdir $(PROTO_OUT)

# Compile proto files to go

<<<<<<< HEAD
grpc: gogo-grpc fix-path
=======
grpc: go-grpc gogo-grpc
>>>>>>> ae84a80... Restructure to be proper package

go-grpc: clean $(PROTO_OUT)
	echo "Compiling for go-gRPC..."
	$(foreach PROTO_DIR,$(PROTO_DIRS),protoc --proto_path=$(PROTO_IMPORT) --go_out=plugins=grpc,paths=source_relative:$(PROTO_OUT) $(PROTO_DIR)*.proto;)

gogo-grpc: clean $(PROTO_OUT)
	echo "Compiling for gogo-gRPC..."
<<<<<<< HEAD
	$(foreach PROTO_DIR,$(PROTO_DIRS),protoc --proto_path=$(PROTO_IMPORT) --gogoslick_out=Mgoogle/protobuf/wrappers.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,plugins=grpc,paths=source_relative:$(PROTO_OUT) $(PROTO_DIR)*.proto;)

fix-path:
	mv -f $(PROTO_OUT)/temporal/* $(PROTO_OUT) && rm -d $(PROTO_OUT)/temporal
=======
	$(foreach PROTO_DIR,$(PROTO_DIRS),protoc --proto_path=$(PROTO_IMPORT) --gogofaster_out=Mgoogle/protobuf/wrappers.proto=github.com/gogo/protobuf/types,Mgoogle/protobuf/timestamp.proto=github.com/gogo/protobuf/types,plugins=grpc,paths=source_relative:$(PROTO_OUT) $(PROTO_DIR)*.proto;)
>>>>>>> ae84a80... Restructure to be proper package

# Plugins & tools

grpc-install: gogo-protobuf-install
	echo "Installing/updaing gRPC plugins..."
	go get -u google.golang.org/grpc

gogo-protobuf-install: go-protobuf-install
<<<<<<< HEAD
	go get -u github.com/temporalio/gogo-protobuf/protoc-gen-gogoslick
=======
	go get -u github.com/gogo/protobuf/protoc-gen-gogofaster
>>>>>>> ae84a80... Restructure to be proper package

go-protobuf-install:
	go get -u github.com/golang/protobuf/protoc-gen-go

<<<<<<< HEAD
# Clean
=======
# clean
>>>>>>> ae84a80... Restructure to be proper package

clean:
	echo "Deleting generated go files..."
	rm -rf $(PROTO_OUT)
