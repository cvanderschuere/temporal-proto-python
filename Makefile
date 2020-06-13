PROTO_ROOT := proto/temporal

# List only subdirectories with *.proto files. Sort to remove duplicates.
PROTO_DIRS = $(sort $(dir $(wildcard $(PROTO_ROOT)/*/*/*.proto)))
PROTO_SERVICES = $(wildcard $(PROTO_ROOT)/*/*/service.proto)


all:
	rm -rf temporal
	$(foreach PROTO_DIR,$(PROTO_DIRS),\
		docker run -v `pwd`:/defs namely/protoc-all:1.29_1 -i proto -d $(PROTO_DIR)  -o . -l python;\
	)
	
