# Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

- **25.3**
- 24.3.1
- 24.2.1
- 23.3.1

```bash
# Lift docker container
docker run -it --entrypoint bash python:3.13

# To know pip version
pip --version
```
*Asnwer: 25.3*

