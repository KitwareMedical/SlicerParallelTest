#include "ParallelTestCppCLICLP.h"

// ITK includes
#include <itksys/SystemTools.hxx>

// STD includes
#include <iostream>

// sleep() function includes
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

namespace{
void startFilter(const std::string& filterName)
{
  std::string startTime = itksys::SystemTools::GetCurrentDateTime("%H:%M:%S");

  std::cout << "Starting " << filterName << " at " << startTime <<  std::endl << std::flush;

  std::cout << "<filter-start>"
            << "<filter-name>" << filterName << "</filter-name>"
            << "<filter-comment>" << filterName << "started at " << startTime << "</filter-comment>"
            << "</filter-start>" << std::endl << std::flush;
}

void reportFilterProgress(const std::string& filterName, int currentStep, int numberOfSteps)
{
  std::cout << "Step " << currentStep << " of " << filterName << std::endl << std::flush;

  float progress = 1.0 / static_cast<float>(numberOfSteps);
  std::cout << "<filter-progress>"
            << (currentStep) * progress
            << "</filter-progress>"
            << std::endl
            << std::flush;
}

void endFilter(const std::string& filterName)
{
  std::string endTime = itksys::SystemTools::GetCurrentDateTime("%H:%M:%S");

  std::cout << "Ending " << filterName << " at "<< endTime <<  std::endl << std::flush;

  std::cout << "<filter-end>"
            << "<filter-name>" << filterName << "</filter-name>"
            << "</filter-end>" << std::endl << std::flush;
}
}

int main( int argc, char * argv[] )
{

  PARSE_ARGS;

  startFilter(name);

  for (int step = 0; step < numberOfSteps; ++step)
    {
    reportFilterProgress(name, step, numberOfSteps);
    sleep(1);
    }

  endFilter(name);

  return EXIT_SUCCESS;
}
