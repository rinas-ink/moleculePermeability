from s4dd import S4forDenovoDesign

# Create an S4 model with (almost) the same parameters in the paper.
s4 = S4forDenovoDesign(
    n_max_epochs=1,  # This is for only demonstration purposes. Set this to a (much) higher value for actual training. Default: 400.
    batch_size=64,  # This is also for demonstration purposes. The value in the paper is 2048.
    device="cpu",  # Replace this with "cpu" if you didn't install pytorch with CUDA support.
)
# Pretrain the model on ChEMBL
s4.train(
    training_molecules_path="./datasets/chemblv31/mini_train.zip",  # This a 50K subsample of the ChEMBL training set for quick(er) testing.
    val_molecules_path="./datasets/chemblv31/valid.zip",
)
# Fine-tune the model on bioactive molecules for PKM2
s4.train(
    training_molecules_path="./datasets/pkm2/train.zip",
    val_molecules_path="./datasets/pkm2/valid.zip",
)
# Design new molecules
designs, lls = s4.design_molecules(n_designs=32, batch_size=16, temperature=1.0)