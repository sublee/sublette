from torchgpipe import GPipe

# Prepare a sequential model.
model = nn.Sequential(a, b, c, d)

# Wrap your model with GPipe.
model = GPipe(model, balance=[1, 1, 1, 1], chunks=8)

for input in data_loader:
    output = model(input)
