FROM python:3.10
RUN pip install uv
RUN --mount=source=dist,target=/dist uv pip install --no-cache --system /dist/*.whl
WORKDIR /app
COPY api.json .
COPY providers.json .
CMD python -m
