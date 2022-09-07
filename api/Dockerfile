# https://colab.research.google.com/drive/10ZAdEwHDbL1lVcUGeCdj9FxXnQSNFSH4?usp=sharing
# https://www.medi-08-data-06.work/entry/machine-learning-api

FROM python:3.8-buster AS builder

COPY requirements.txt .
RUN pip install awslambdaric && \
    pip install -r requirements.txt

WORKDIR /content

# installing dependencies
RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    wget \
    unzip \
    libprotobuf-dev \
    protobuf-compiler && \
    wget https://download.pytorch.org/libtorch/cu102/libtorch-cxx11-abi-shared-with-deps-1.8.1%2Bcu102.zip && \
    unzip -o libtorch-cxx11-abi-shared-with-deps-1.8.1+cu102.zip

# downloading source code
RUN rm -rf MMM_API && \
    rm -rf MMM_API_SEP_2.zip && \
    wget https://www.sfu.ca/~jeffe/MMM_API_SEP_2.zip && \
    unzip -o MMM_API_SEP_2.zip

# downloading model
RUN wget -O model.pt http://vault.sfu.ca/index.php/s/Ff2j19IrKS5R969/download

WORKDIR /content/MMM_API

# installing mmm-api (takes a few minutes)
RUN ["/bin/bash", "-c", "bash build_python_google.sh --google"]
WORKDIR /content/MMM_API/python
RUN pip install .

# installing python modules
RUN pip install pyFluidSynth && \
    apt install -y fluidsynth && \
    pip install midi2audio && \
    cp /usr/share/sounds/sf2/FluidR3_GM.sf2 ./font.sf2

WORKDIR /

FROM python:3.8-slim-buster
ARG APP_DIR="/home/app/"

COPY app/* ${APP_DIR}
WORKDIR ${APP_DIR}
COPY --from=builder  /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages/
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]