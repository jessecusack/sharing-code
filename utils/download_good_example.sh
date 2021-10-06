cd ..
mkdir good_example
cd good_example
git clone https://github.com/jessecusack/example_research_project
cd example_research_project/setup_scripts
./setup.sh
./remove_environment.sh
cd ..
rm -rf .git setup_scripts environment.yml .gitignore matlab_toolboxes/m_map/doc matlab_toolboxes/download*.* data/download*.* data/external/.gitkeep
cd ..
mv example_research_project/* .
rm -rf example_research_projects